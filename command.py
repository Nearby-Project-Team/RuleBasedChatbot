from model.nearby_chatbot import NearbyLogic
import argparse

RuleChatModel = NearbyLogic()
parser = argparse.ArgumentParser(description='This SW is for debugging Rule Based Chatbot')
parser.add_argument('--elderly_id', help='Elderly ID')

# sample elderly_id: 18df3a24-2094-4148-957e-9e36a3d8eab4 , 4bfd27d9-ebf5-43ff-afff-e42adc8dfd82
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
