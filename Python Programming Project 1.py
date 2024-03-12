class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question, options):
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        user_choice = input("Enter your choice (1-4): ")
        return user_choice

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect! The correct answer is:", correct_answer)

    def start_quiz(self):
        print("Welcome to the PhD-level Quiz in Biotechnology and Neuroscience!")
        print("Answer the following challenging questions:")

        for i, (question, options, correct_answer) in enumerate(self.questions, 1):
            print("\nQuestion", i)
            user_choice = self.display_question(question, options)
            self.evaluate_answer(user_choice, correct_answer)

        print("\nQuiz complete!")
        print("Your final score is:", self.score)


if __name__ == "__main__":
    questions = [
        ("Which enzyme is commonly used for DNA amplification in PCR?", ["Helicase", "Topoisomerase", "Polymerase", "Ligase"], "3"),
        ("What is the primary function of the hippocampus in the brain?", ["Memory formation", "Vision processing", "Emotional regulation", "Motor control"], "1"),
        ("Which neurotransmitter is primarily associated with reward and pleasure?", ["Dopamine", "Serotonin", "GABA", "Glutamate"], "1"),
        ("What is the main function of the CRISPR/Cas9 system in biotechnology?", ["Gene editing", "Metabolism regulation", "Protein synthesis", "Cell signaling"], "1"),
        ("Which technique is used to visualize brain activity in real-time?", ["PCR", "fMRI", "ELISA", "Western blotting"], "2"),
        ("What is the purpose of optogenetics in neuroscience research?", ["Control of neuronal activity with light", "DNA sequencing", "Cell cloning", "Drug delivery"], "1"),
        ("Which structure connects the two hemispheres of the brain?", ["Corpus callosum", "Cerebellum", "Thalamus", "Hypothalamus"], "1")
    ]
    quiz = Quiz(questions)
    quiz.start_quiz()
