from pgmpy.models import BayesianModel
from pgmpy.readwrite import NETReader
from pgmpy.inference import VariableElimination

class RouteRiskBayesNet:
    def __init__(self, path):
        self.model: BayesianModel = NETReader(path).get_model()
        self.infer: VariableElimination = VariableElimination(self.model)
        self.variables: set[str] = {"risk"}

    def predict(self, evidence: dict[str, str]):
        result = self.infer.map_query(
            variables=self.variables,
            evidence=evidence,
            show_progress=False
        )
        return result
