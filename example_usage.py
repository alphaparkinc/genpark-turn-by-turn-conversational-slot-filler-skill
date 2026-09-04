from client import TurnByTurnConversationalSlotFillerClient

def main():
    client = TurnByTurnConversationalSlotFillerClient()
    res = client.extract_slots('Reserve haircut tomorrow at noon')
    print('Slot Filler: ' + res['extraction_id'] + ' (Complete: ' + str(res['slot_fulfillment_complete']) + ')')
    print('Filled Slots: ' + str(res['filled_slots']))
    print('Profile URL: ' + res['slot_profile_url'])

if __name__ == '__main__':
    main()
