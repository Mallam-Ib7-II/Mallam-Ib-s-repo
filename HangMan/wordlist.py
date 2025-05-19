import random


WORD_LIST_CATEGORIES = {
    'animals' : (
    "aardvark", "albatross", "alligator", "alpaca", "ant", "antelope", "ape", "armadillo", "baboon", "badger", 
    "barracuda", "bat", "bear", "beaver", "bee", "beetle", "bird", "bison", "boar", "butterfly", "camel", 
    "canary", "caribou", "cat", "caterpillar", "cheetah", "chicken", "chimpanzee", "chinchilla", "cobra", 
    "cod", "condor", "cougar", "cow", "coyote", "crab", "crane", "crocodile", "crow", "deer", "dingo", 
    "dog", "dolphin", "dove", "dragonfly", "duck", "eagle", "eel", "elephant", "elk", "emu", "falcon", 
    "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gazelle", "gecko", "gerbil", "giraffe", 
    "goat", "goldfish", "goose", "gorilla", "grouse", "guinea pig", "hamster", "hawk", "hedgehog", 
    "hippopotamus", "horse", "hummingbird", "hyena", "iguana", "impala", "jackal", "jaguar", "jay", 
    "jellyfish", "kangaroo", "kingfisher", "koala", "komodo dragon", "ladybug", "lemur", "leopard", 
    "lion", "lizard", "llama", "lobster", "loon", "macaque", "magpie", "manatee", "marmot", "mongoose", 
    "monkey", "moose", "mosquito", "moth", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", 
    "opossum", "ostrich", "otter", "owl", "ox", "panda", "parrot", "peacock", "penguin", "pheasant", 
    "pig", "pigeon", "platypus", "polar bear", "porcupine", "possum", "prairie dog", "quail", "rabbit", 
    "raccoon", "rat", "raven", "reindeer", "rhinoceros", "robin", "salmon", "salamander", "seal", 
    "shark", "sheep", "shrimp", "skunk", "sloth", "snail", "snake", "sparrow", "spider", "squid", 
    "squirrel", "starfish", "stingray", "swan", "swordfish", "tapir", "tiger", "toad", "turkey", 
    "turtle", "walrus", "wasp", "weasel", "whale", "wolf", "wombat", "woodpecker", "worm", "zebra"
),
    'places' : (
    "Paris", "Tokyo", "London", "Rome", "Sydney", "Cairo", "Athens", "Kyoto", "Venice", "Berlin", 
    "Madrid", "Vienna", "Prague", "Dublin", "Lisbon", "Oslo", "Copenhagen", "Stockholm", "Helsinki", "Amsterdam", 
    "Budapest", "Istanbul", "Moscow", "NewYork", "Chicago", "LosAngeles", "Seattle", "Miami", "Boston", "SanFrancisco",
    "Dallas", "Houston", "Phoenix", "Atlanta", "Philadelphia", "Detroit", "Denver", "SanDiego", "Minneapolis", "Portland", 
    "Cleveland", "Baltimore", "StLouis", "KansasCity", "LasVegas", "Orlando", "NewOrleans", "Nashville", "Charlotte", "Columbus",
    "Phoenix", "Alcatraz", "Galapagos", "Amazon", "Serengeti", "Everest", "Sahara", "Gobi", "Kalahari", "Antarctica",
    "Arctic", "Ocean", "River", "Forest", "Desert", "Island", "Mountain", "Valley", "Canyon", "Lake", 
    "Plains", "Jungle", "Meadow", "Volcano", "Cave", "Beach", "Shore", "Cliff", "Peak", "Ridge", 
    "Oasis", "Haven", "Eden", "Elysium", "Avalon", "ShangriLa", "Camelot", "Oz", "Narnia", "Wonderland",
    "Asgard", "Olympus", "Valhalla", "Tartarus", "Hades", "Nirvana", "Heaven", "Hell", "Void", "Abyss",
    "Cosmos", "Infinity", "Nowhere", "Everywhere", "Here", "There", "Beyond", "Within", "Above", "Below"
),
    'things' : (
    "Book", "Phone", "Coffee", "Music", "Sun", "Moon", "Star", "Rain", "Wind", "Fire",
    "Water", "Earth", "Tree", "Flower", "Bird", "Dog", "Cat", "Dream", "Hope", "Love",
    "Fear", "Anger", "Joy", "Sadness", "Time", "Space", "Light", "Shadow", "Truth", "Lie",
    "Story", "Poem", "Song", "Dance", "Art", "Science", "History", "Mystery", "Magic", "Wonder",
    "Puzzle", "Game", "Challenge", "Victory", "Defeat", "Journey", "Adventure", "Discovery", "Innovation", "Creation",
    "Destruction", "Chaos", "Order", "Balance", "Harmony", "Dissonance", "Rhythm", "Melody", "Silence", "Noise",
    "Color", "Shape", "Texture", "Taste", "Smell", "Touch", "Sight", "Hearing", "Feeling", "Thinking",
    "Imagination", "Memory", "Knowledge", "Wisdom", "Experience", "Intuition", "Inspiration", "Motivation", "Passion", "Desire",
    "Goal", "Purpose", "Meaning", "Value", "Belief", "Doubt", "Faith", "Hope", "Love", "Kindness",
    "Compassion", "Empathy", "Gratitude", "Forgiveness", "Peace", "War", "Justice", "Freedom", "Equality", "Diversity",
    "Unity", "Community", "Family", "Friendship", "Connection", "Disconnection", "Isolation", "Loneliness", "Happiness", "Sadness",
    "Joy", "Pain", "Suffering", "Healing", "Growth", "Change", "Transformation", "Evolution", "Revolution", "Reformation",
    "Revolution", "Reformation", "Destiny", "Fate", "Chance", "Choice", "Action", "Reaction", "Consequence", "Outcome",
    "Beginning", "End", "Now", "Then", "Forever", "Never", "Maybe", "Perhaps", "Certainly", "Definitely"
),
    'names' : (
    "Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Iris", "Jack",
    "Katie", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Samuel", "Tara",
    "Ulysses", "Violet", "William", "Xander", "Yara", "Zachary", "Anya", "Blake", "Cameron", "Dakota",
    "Eleanor", "Finn", "Gemma", "Harper", "Indigo", "Jasper", "Kai", "Lena", "Mateo", "Nora",
    "Oliver", "Penelope", "Quentin", "Rowan", "Sasha", "Thomas", "Uma", "Victor", "Willow", "Xavier",
    "Yvette", "Zephyr", "Aaliyah", "Benjamin", "Clara", "Daniel", "Evelyn", "Felix", "Giselle", "Hugo",
    "Isla", "Julian", "Kiana", "Leo", "Maya", "Nathan", "Ophelia", "Parker", "Quinn", "Riley",
    "Sophia", "Theo", "Ursula", "Vincent", "Willow", "Xander", "Yara", "Zephyr", "Aiden", "Bella",
    "Caleb", "Daisy", "Ethan", "Fiona", "Gabriel", "Hazel", "Isaac", "Juliet", "Kai", "Lily",
    "Maxwell", "Natalie", "Owen", "Piper", "Quentin", "Rose", "Samuel", "Talia", "Uriah", "Victoria",
    "Walter", "Xenia", "Yvette", "Zachary"
)
}


def hidden_word(word_list):
    word_to_guess = random.choice(word_list)
    return word_to_guess
    

def clue_display(word):
    clue = ['_' for _ in range(len(word))]
    return clue


