""" FLatten """
import json
def main(value: list):
    """ Main function """
    anslist = []
    for raw in value:
        if isinstance(raw, list):
            anslist += main(raw)
        else:
            anslist.append(raw)
    anslist.sort(reverse=True)
    return anslist
print(main(json.loads(input())))
