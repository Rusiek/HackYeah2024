import json

from flask import Flask, request, jsonify
from model import RouteRiskBayesNet

class RouteRisk:
    def __init__(
            self,
            strava_popularity_list: list[int],
            strava_hazardous_list: list[bool],
            here_jam_factor_list: list[float],
            here_flow_speed_list: list[float],
            here_speed_cap_list: list[float],
            model_path: str
        ):
        self.risk_bounds: dict[str, tuple[float, float]] = {
            "strava_popularity": self.__normalize_lists(strava_popularity_list),
            "strava_hazardous": self.__normalize_lists(strava_hazardous_list),
            "here_jam_factor": self.__normalize_lists(here_jam_factor_list),
            "here_flow_speed": self.__normalize_lists(here_flow_speed_list),
            "here_speed_cap": self.__normalize_lists(here_speed_cap_list)
        }
        self.model: RouteRiskBayesNet = RouteRiskBayesNet(model_path)

    def __normalize_lists(self, data: list[float], reverse: bool = False) -> tuple[float, float]:
        data = sorted(data, reverse=True) if reverse else sorted(data)
        lo_bound: float = 0.25
        hi_bound: float = 0.75
        return {
            "lo": data[int(len(data) * lo_bound)],
            "hi": data[int(len(data) * hi_bound)]
        }
    
    def __find_risk(self, val: float, data_type: str, reverse: bool = False) -> str:
        output = "mid"
        try:
            if reverse:
                if val < self.risk_bounds[data_type]["lo"]:
                    output = "lo"
                if val > self.risk_bounds[data_type]["hi"]:
                    output = "hi"
            else:
                if val > self.risk_bounds[data_type]["lo"]:
                    output = "lo"
                if val < self.risk_bounds[data_type]["hi"]:
                    output = "hi"
        except TypeError:
            output = None

        return output

    def __call__(
        self,
        strava_popularity: float,
        strava_hazardous: bool,
        here_jam_factor: float,
        here_flow_speed: float,
        here_speed_cap: float,
    ) -> dict:
        try:
            strava_popularity_risk: str = self.__find_risk(strava_popularity, "strava_popularity")
        except ValueError:
            strava_popularity_risk: str = None

        try:
            strava_hazardous_risk: str = self.__find_risk(strava_hazardous, "strava_hazardous")
        except ValueError:
            strava_hazardous_risk: str = None

        try:    
            here_jam_factor_risk: str = self.__find_risk(here_jam_factor, "here_jam_factor")
        except ValueError:
            here_jam_factor_risk: str = None

        try:
            here_flow_speed_risk: str = self.__find_risk(here_flow_speed, "here_flow_speed")
        except ValueError:
            here_flow_speed_risk: str = None

        try:
            here_speed_cap_risk: str = self.__find_risk(here_speed_cap, "here_speed_cap")
        except ValueError:
            here_speed_cap_risk: str = None

        evidence = {
            "strava_popularity": strava_popularity_risk,
            "strava_hazardous": strava_hazardous_risk,
            "here_jam_factor": here_jam_factor_risk,
            "here_flow_speed": here_flow_speed_risk,
            "here_speed_cap": here_speed_cap_risk
        }
        evidence = {k: v for k, v in evidence.items() if v is not None}
        prediction: dict[str] = self.model.predict(evidence=evidence)

        return prediction
