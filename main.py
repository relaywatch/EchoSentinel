from echo_sentinel import analyze_prompt_chain

example_chain = [
    "This is the most amazing breakthrough we've ever seen.",
    "We're all doomed — nothing can save us now.",
    "Our team has made incredible progress!",
    "I fear this project has completely failed."
]

result = analyze_prompt_chain(example_chain)
print("EchoSentinel Result:")
print(result)

Add main.py runner script
