from js import document

# 20 sample easy aptitude questions
questions = [
    {
        "question": "Which number comes next: 2, 4, 8, 16, ...?",
        "options": ["18", "20", "32", "24"],
        "answer": "32"
    },
    {
        "question": "Find the odd one out: Apple, Banana, Mango, Carrot",
        "options": ["Apple", "Banana", "Mango", "Carrot"],
        "answer": "Carrot"
    },
    {
        "question": "What is 15% of 200?",
        "options": ["20", "25", "30", "35"],
        "answer": "30"
    },
    {
        "question": "If A=1, B=2, ..., what is the value of D+O+G?",
        "options": ["26", "31", "34", "30"],
        "answer": "26"
    },
    {
        "question": "Which one is a prime number?",
        "options": ["9", "15", "17", "21"],
        "answer": "17"
    },
    {
        "question": "If 3x = 12, what is x?",
        "options": ["4", "6", "5", "3"],
        "answer": "4"
    },
    {
        "question": "Which number is missing? 5, 10, ?, 20, 25",
        "options": ["13", "15", "18", "12"],
        "answer": "15"
    },
    {
        "question": "Which day comes after Wednesday?",
        "options": ["Monday", "Tuesday", "Thursday", "Friday"],
        "answer": "Thursday"
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which is the largest planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is 7 x 6?",
        "options": ["42", "36", "48", "38"],
        "answer": "42"
    },
    {
        "question": "If you have 3 dozens, how many items do you have?",
        "options": ["30", "33", "36", "39"],
        "answer": "36"
    },
    {
        "question": "Complete: Cat is to Kitten as Dog is to ____?",
        "options": ["Lion", "Cub", "Puppy", "Goat"],
        "answer": "Puppy"
    },
    {
        "question": "Which shape has 4 equal sides?",
        "options": ["Triangle", "Circle", "Square", "Rectangle"],
        "answer": "Square"
    },
    {
        "question": "How many hours in 2 days?",
        "options": ["24", "36", "48", "60"],
        "answer": "48"
    },
    {
        "question": "Which number is odd?",
        "options": ["2", "4", "6", "7"],
        "answer": "7"
    },
    {
        "question": "Which one is not an animal?",
        "options": ["Tiger", "Lion", "Laptop", "Cat"],
        "answer": "Laptop"
    },
    {
        "question": "Which is heavier: 1kg cotton or 1kg iron?",
        "options": ["Cotton", "Iron", "Same", "Depends"],
        "answer": "Same"
    },
    {
        "question": "What is next: A, C, E, G, __?",
        "options": ["I", "H", "J", "K"],
        "answer": "I"
    },
    {
        "question": "What is 100 divided by 5?",
        "options": ["20", "25", "15", "30"],
        "answer": "20"
    }
]

# Render the quiz questions on load
quiz_form = document.getElementById("quiz-form")

for i, q in enumerate(questions):
    div = document.createElement("div")
    div.classList.add("question")
    div.innerHTML = f"<strong>Q{i+1}. {q['question']}</strong><div class='options'></div>"
    
    options_div = div.querySelector(".options")
    for opt in q["options"]:
        option_id = f"q{i}_{opt}"
        radio_html = f"""
        <label>
          <input type="radio" name="q{i}" value="{opt}" id="{option_id}"> {opt}
        </label>
        """
        options_div.innerHTML += radio_html

    quiz_form.appendChild(div)

# Score calculator
def calculate_score():
    score = 0
    for i, q in enumerate(questions):
        options = document.getElementsByName(f"q{i}")
        for opt in options:
            if opt.checked:
                if opt.value == q["answer"]:
                    score += 1
                break
    document.getElementById("score-output").innerText = f"✅ Your score: {score} / 20"
