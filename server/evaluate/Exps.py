from evaluate.Exp import Exp
from evaluate.RetrieveTest import run_tests
from vector_db.TestCases import retrieve_baseline, retrieve_e1, retrieve_e2, retrieve_e3, retrieve_e4, retrieve_full


class Exp4k(Exp):
    def run_exp(self):
        for k in  [25]:
            test_cases = self.prepare_case("evaluate/questions.txt", k, "测试最佳k值")
            run_tests(
                retrieve=retrieve_baseline,
                test_cases=test_cases,
                output_json=f"./statistics/topk/topk_results_{k}.json",
                output_csv=f"./statistics/topk/topk_summary_{k}.csv",
            )


class Exp4ablation(Exp):
    def run_exp(self):
        test_cases = self.prepare_case("evaluate/questions.txt", 10, "消融实验")
        # run_tests(
        #     retrieve=retrieve_baseline,
        #     test_cases=test_cases,
        #     output_json="./statistics/ablation_baseline.json",
        #     output_csv="./statistics/ablation_baseline.csv",
        # )
        run_tests(
            retrieve=retrieve_e1,
            test_cases=test_cases,
            output_json="./statistics/ablation_e1.json",
            output_csv="./statistics/ablation_e1.csv",
        )
        run_tests(
            retrieve=retrieve_e2,
            test_cases=test_cases,
            output_json="./statistics/ablation_e2.json",
            output_csv="./statistics/ablation_e2.csv",
        )
        run_tests(
            retrieve=retrieve_e3,
            test_cases=test_cases,
            output_json="./statistics/ablation_e3.json",
            output_csv="./statistics/ablation_e3.csv",
        )
        run_tests(
            retrieve=retrieve_e4,
            test_cases=test_cases,
            output_json="./statistics/ablation_e4.json",
            output_csv="./statistics/ablation_e4.csv",
        )
        run_tests(
            retrieve=retrieve_full,
            test_cases=test_cases,
            output_json="./statistics/ablation_full.json",
            output_csv="./statistics/ablation_full.csv",
        )
