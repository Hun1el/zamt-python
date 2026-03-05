def make_sandvitch(*components):
    print("Сэндвич:")
    for component in components:
        print("-", component)
make_sandvitch("Хлеб", "Муравей")
make_sandvitch("Хлеб", "Свинина")

def make_sandvitch(*components):
    print("Сэндвич:")
    for component in components:
        print("-", component)

make_sandvitch("Хлеб", "Муравей")
make_sandvitch("Хлеб", "Свинина")
