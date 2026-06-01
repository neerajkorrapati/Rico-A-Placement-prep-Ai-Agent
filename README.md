day 0: Turn ai-generated text into structured app data.
day 1: Conversational Ai-Systems, (basically with context, built using chat[] declared outside while loop)
day 2: Reliable validated Ai- pipelines, (instead of directly relying on ai- outpus, we validate it through a pre-determined structure using pydantic, and generate the preferred response.)
day 3: Persistent Ai-Systems, App's no longer behave like a temporary script, start behaving like Ai-assistants,
      ~we convert the the chat_history into json files, and store it inside the computer's memory ,such that even if we quit the program and relaunch it , it will have context.
      (implementation and understanding of context windows, file serialzaition -(converting python objets into solvable formats)
      ~functions to trim -memory() to reduce token,memory and load usage
day 4:Gemini-router implementation,
      ~intially gemini was acting as a text generator, but here we make it act as an ai agent,
      we give it pre-made tools, and it chooses from these existing tools and executes the operation at hand, hence acting like a true Ai_Agent.
      (here we also implement the parsing function).
