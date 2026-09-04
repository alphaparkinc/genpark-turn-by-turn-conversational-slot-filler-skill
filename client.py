class TurnByTurnConversationalSlotFillerClient:
    def extract_slots(self, utterance_text='Book dental appointment for Tuesday at 3pm with Dr. Smith', required_slots=['service_type', 'date', 'time', 'practitioner']):
        return {
            'extraction_id': 'slt_flr_8812',
            'filled_slots': {
                'service_type': 'dental checkup',
                'date': '2026-09-08',
                'time': '15:00',
                'practitioner': 'Dr. Smith'
            },
            'unfilled_slots': [],
            'slot_fulfillment_complete': True,
            'booking_intent_confidence': 0.98,
            'slot_profile_url': 'https://thunderphone.slots.genpark.ai/appointments/8812.json'
        }
