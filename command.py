from model.nearby_chatbot import NearbyLogic
import argparse

RuleChatModel = NearbyLogic()
parser = argparse.ArgumentParser(description='This SW is for debugging Rule Based Chatbot')
parser.add_argument('--elderly_id', help='Elderly ID')

if __name__ == "__main__":
    args = parser.parse_args()
    elderly_id = args.elderly_id
    while True:
        try:
            user = input("User> ")
            res = RuleChatModel.process(user, elderly_id)
            print("Chatbot> " + str(res))
        except KeyboardInterrupt:
            print("\nExit.")
            break
