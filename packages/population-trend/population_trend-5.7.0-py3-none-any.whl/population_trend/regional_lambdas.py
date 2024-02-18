import numpy as np
import json

from bootstrapping_tools import calculate_intervals_from_p_values_and_alpha

from population_trend.calculate_growth_rates import Bootstrap_from_time_series


class Island_Bootstrap_Distribution_Concatenator:
    def __init__(self, paths):
        self.paths_string = paths

    def read_json_file(self, path):
        with open(path) as json_file:
            json_content = json.load(json_file)
        return json_content

    def _extract_paths_from_region(self, region):
        config_content = self.read_json_file(self.paths_string)
        clean_paths = config_content[region]["paths"]
        return clean_paths

    def set_region(self, region):
        self.region = region
        self.distributions = self.extract_distributions()

    def read_json_files(self):
        splited_paths = self._extract_paths_from_region(self.region)
        json_list = []
        for path in splited_paths:
            json_content = self.read_json_file(path)
            json_list.append(json_content)
        return json_list

    def extract_distributions(self):
        json_list = self.read_json_files()
        distributions = [self._read_distribution(json_content) for json_content in json_list]
        return distributions

    def mean_by_row(self):
        return np.mean(self._concatenate_distribution(*self.distributions), axis=1)

    def _concatenate_distribution(self, *argv):
        rng = np.random.default_rng(seed=42)
        list_of_distributions = []
        for arg in argv:
            resampled = rng.choice(arg, size=2000, replace=True)
            list_of_distributions.append(resampled)
        return np.array(list_of_distributions).T

    def _read_distribution(self, json_dict):
        completed_distribution = json_dict["bootstrap_intermediate_distribution"]
        lambdas_distribution = [sample[0] for sample in completed_distribution]
        return lambdas_distribution


class Calculator_Regional_Lambdas_Intervals(Bootstrap_from_time_series):
    def __init__(self, regional_lambdas, alpha):
        self.lambdas = regional_lambdas
        self.p_values = self.get_p_values()
        self.alpha = alpha
        self.intervals = self.intervals_from_p_values_and_alpha()
        self.interval_lambdas = [interval for interval in self.intervals]
        self.lambda_latex_interval = self.get_lambda_interval_latex_string()
        self.hypothesis_test_statement_latex = self.get_hypotesis_statement()
        self.hypothesis_test_statement_latex_en = self.get_hypotesis_statement_en()

    def intervals_from_p_values_and_alpha(self):
        intervals = calculate_intervals_from_p_values_and_alpha(
            self.lambdas, self.p_values, self.alpha
        )
        return intervals

    def get_intermediate_lambdas(self):
        return [
            lambdas
            for lambdas in self.lambdas
            if (lambdas > self.intervals[0]) and (lambdas < self.intervals[2])
        ]

    def get_hypotesis_statement(self):
        rounded_p_values = np.round(self.p_values, 3)
        if self.p_values[1] < self.alpha:
            return f"La población está decreciendo. $H_0: \\lambda > 1$, $\\alpha > p =$ {rounded_p_values[1]}"
        if self.p_values[0] < self.alpha:
            return f"La población está creciendo. $H_0: \\lambda < 1$, $\\alpha > p =$ {rounded_p_values[0]}"
        return (
            "El valor $p$ calculado resultó mayor que $\\alpha$ en las dos hipótesis nulas probadas"
        )

    def get_hypotesis_statement_en(self):
        rounded_p_values = np.round(self.p_values, 3)
        if self.p_values[1] < self.alpha:
            return f"The population is decreasing. $H_0: \\lambda > 1$, $\\alpha > p =$ {rounded_p_values[1]}"
        if self.p_values[0] < self.alpha:
            return f"The population is increasing. $H_0: \\lambda < 1$, $\\alpha > p =$ {rounded_p_values[0]}"
        return "The calculated $p$-value is higher than the $\\alpha$ in both null hypothesis tests"

    def save_intervals(self, output_path):
        json_dict = {
            "intervals": list(self.intervals),
            "lambda_latex_interval": self.lambda_latex_interval,
            "p-values": self.p_values,
            "bootstrap_intermediate_distribution": self.get_intermediate_lambdas(),
            "hypothesis_test_statement_latex_sp": self.hypothesis_test_statement_latex,
            "hypothesis_test_statement_latex_en": self.hypothesis_test_statement_latex_en,
        }
        with open(output_path, "w") as file:
            json.dump(json_dict, file)
