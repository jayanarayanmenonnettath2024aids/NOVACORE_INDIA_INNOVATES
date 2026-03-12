import time

def trigger_outbound_call(ticket_id, reason):
    """
    Simulates an AI-initiated call to a citizen.
    """
    print(f"\n--- [OUTBOUND CALL INITIATED] ---")
    print(f"Target Ticket ID: {ticket_id}")
    print(f"Reason: {reason}")
    print(f"Status: Connecting...")
    time.sleep(2)
    print(f"AI: 'Hello, I am PALLAVI from the Citizen Support Center. I am calling regarding your {reason}.'")
    print(f"AI: 'Your request is currently being processed by the assigned department.'")
    print(f"Status: Call Completed successfully.\n")
