from parserr import parserAB


def main():
    parser = parserAB(
    'https://atlasbus.by/',
    'Ваня',
    'Летающий',
    '+375296766767',
    'Минск',
    'Витебск',
    '30 октября'
    )
    parser.acceptCoockie()
    parser.openBus()



if __name__ == "__main__":
    main()