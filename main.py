from echo_sentinel import analyze_prompt_chain

# Optional: insert your test Webhook.site URL below
webhook_url = "https://webhook.site/833440dc-c6d5-472e-8b76-3206541438fa"

example_chain = [
    "This is the most amazing breakthrough we've ever seen.",
    "We're all doomed – nothing can save us now.",
    "Our team has made incredible progress!",
    "I fear this project has completely failed."
]

result = analyze_prompt_chain(example_chain, webhook_url=webhook_url)
print("EchoSentinel Result:")
print(result)
