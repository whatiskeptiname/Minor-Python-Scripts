from pubsub import pub


def listener_alice(arg):
    print("Alice receives news about", arg["headline"])
    print(arg["news"])
    print()


def listener_bob(arg):
    print("Bob receives news about", arg["headline"])
    print(arg["news"])
    print()


# Register listeners
pub.subscribe(listener_alice, "football")
pub.subscribe(listener_alice, "chess")
pub.subscribe(listener_bob, "football")

# Send messages to all listeners of topics
pub.sendMessage("football", arg={"headline": "Ronaldo", "news": "Sold for $1M"})
pub.sendMessage(
    "chess", arg={"headline": "AI", "news": "AlphaZero beats grandmaster Carlsen"}
)
