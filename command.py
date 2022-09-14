from model.nearby_chatbot import NearbyLogic
import argparse

RuleChatModel = NearbyLogic()
parser = argparse.ArgumentParser(description='This SW is for debugging Rule Based Chatbot')
parser.add_argument('--elderly_id', help='Elderly ID')

# sample elderly_id: 26f0e561-f107-4870-a11f-0e5ad78a19c0 , 083c11d7-be91-4903-99ce-5b3eaa62beb1
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
