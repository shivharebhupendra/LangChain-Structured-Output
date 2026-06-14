from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional, Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""I have been using the Apple MacBook Air M3 (13-inch, 16GB RAM, 512GB SSD) for about three months as my primary laptop for work, learning machine learning, content creation, and general productivity tasks.

The first thing that impressed me was the performance. The M3 chip handles everyday tasks effortlessly, including running multiple browser tabs, Python development environments, Jupyter notebooks, VS Code, and even light video editing. Applications launch almost instantly, and the system remains responsive even under heavy multitasking.

Battery life is one of the strongest aspects of this laptop. On a typical workday involving web browsing, coding, document editing, and video streaming, I consistently get around 14-16 hours of usage on a single charge. This means I rarely need to carry the charger when working outside.

The display quality is excellent. The Retina display produces sharp text, vibrant colors, and good brightness levels, making it comfortable for long coding sessions and media consumption. The keyboard is also comfortable, with good key travel and a responsive typing experience.

The laptop is extremely lightweight and portable. Carrying it in a backpack all day is effortless, which makes it ideal for students and professionals who travel frequently.

However, there are some drawbacks. The base configuration is expensive compared to many Windows laptops offering similar storage and RAM. Upgrading RAM or SSD at purchase time significantly increases the price. Another limitation is the limited number of ports. Having only two USB-C ports means users may need to purchase additional adapters or hubs.

Gaming performance is better than previous MacBook Air models, but it still cannot compete with dedicated gaming laptops. Some specialized software and games remain unavailable or less optimized on macOS compared to Windows.

The webcam and speakers are good for video calls and entertainment, but they are not industry-leading. Users seeking professional-grade audio or video production may still need external equipment.

Overall, the MacBook Air M3 is an excellent laptop for students, software developers, content creators, and professionals who prioritize portability, battery life, and smooth performance. While the price and limited ports may discourage some buyers, the overall user experience is outstanding, making it one of the best ultraportable laptops currently available.

Pros
Excellent battery life (14-16 hours)
Fast and efficient M3 chip
Lightweight and highly portable
Premium build quality
Beautiful Retina display
Silent operation (fanless design)
Cons
Expensive upgrades
Only two USB-C ports
Limited gaming support
Some software compatibility issues
Accessories and adapters increase overall cost""")

print(result)
