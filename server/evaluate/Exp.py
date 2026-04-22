from evaluate.RetrieveTest import TestCase


class Exp:
    def prepare_case(self, questions_path: str, k: list[int] | int, desc) -> list[TestCase]:
        questions = self._read_questions(questions_path)
        if type(k) == int:
            k_list = [k] * len(questions)
        else:
            k_list = k
        if len(questions) > len(k_list):
            questions = questions[:len(k_list)]
        cases = []
        for i, question in enumerate(questions):
            case = TestCase(
                query=question,
                k=k_list[i],
                description=desc,
            )
            cases.append(case)
        return cases

    def _read_questions(self, questions_path: str) -> list[str]:
        questions = []
        with open(questions_path, 'r', encoding='utf-8') as f:
            for line in f:
                question = line.strip()
                if question:  # 可选：过滤空行
                    questions.append(question)
        return questions
