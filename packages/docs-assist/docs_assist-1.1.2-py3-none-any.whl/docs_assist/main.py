from openai import OpenAI
from time import sleep
class Assistant:
  def __init__(self,api_key):
    self.api_key = api_key
    self.client = OpenAI(api_key=self.api_key)


  def config(self,file_path:str,file_purpose:str = 'assistants',assistant_name:str="Personal Assistant",system_instructions = 'You are a personal assistant that answer the user queries from the file uploaded.',model='gpt-3.5-turbo-1106',tools:list[dict] = [{'type':'retrieval'}],thread_instructions:str="Please address the user as a student"):
    print(file_path)
    self.file_path = file_path
    self.file_purpose = file_purpose
    self.model = model
    self.tools = tools
    self.thread_instructions = thread_instructions
    self.system_instructions = system_instructions
    self.assistant_name = assistant_name

    # Initial Setup for API key

    # Step 1- Create a file
    self.file = self.client.files.create(
        purpose=self.file_purpose,
        file=open(self.file_path,'rb')
    )

    # Step 2- Create Assistant
    self.assistant = self.client.beta.assistants.create(
        name=self.assistant_name,
        instructions = self.system_instructions,
        model = self.model,
        tools = self.tools,
        file_ids=[self.file.id]

    )



    # Step 3- Create a thread
    self.thread = self.client.beta.threads.create()

  def ask(self,user_query:str):
    # Step 4- Create a message
    self.message = self.client.beta.threads.messages.create(
        thread_id=self.thread.id,
        role='user',
        content=user_query
    )

    # Step 5- Run the thread
    self.run = self.client.beta.threads.runs.create(
        assistant_id = self.assistant.id,
        thread_id = self.thread.id,
        instructions = self.thread_instructions
    )


    if self.run_status(): # Step 6- Check the run status
      # then display the messages
      # Step 7- Display the messages:
      sleep(5)
      self.display_messages()
    else:
      print("Thread was not completely run. There may be problems")


  def run_status(self):

    while True:
      sleep(3)
      status = self.client.beta.threads.runs.retrieve(run_id=self.run.id,thread_id=self.thread.id).status

      print("Status:\t",status)
      if  status=='completed':
        return True
      elif status in ['failed','cancelled','expired']:        
        return False
      
        
  
  def display_messages(self):
    self.messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
    print(self.messages.data)
    print()
    print()
    # display the messages in reversed order
    for message in reversed(self.messages.data):
      print(message.role + ": " + message.content[0].text.value)



  #terminate only deletes the current file, thread and assistant
  def terminate(self):
    # Delete assistant file
    delete_file = self.client.beta.assistants.files.delete(file_id=self.file.id, assistant_id=self.assistant.id)
    print(delete_file)

    # delete thread
    delete_thread = self.client.beta.threads.delete(thread_id=self.thread.id)
    print(delete_thread)
    # Delete assistant
    deleted_assistant = self.client.beta.assistants.delete(assistant_id=self.assistant.id)
    print(deleted_assistant)

  # this method deletes all the associated assistants with the client
  def delete_all_assistants(self):
    assistants = self.client.beta.assistants.list().data
    for assistant in assistants:
      self.client.beta.assistants.delete(assistant_id=assistant.id)

    print("All assistants have been successfully deleted.")

  # this method deletes all the associated files from the client
  def delete_all_files(self):
    files = self.client.files.list().data
    for file in files:
      self.client.files.delete(file_id=file.id)

    print("All files have been successfully deleted")

  # this method deletes all the files, and assistants
  def delete_all(self):
    # delete the files
    self.delete_all_files()

    # delete all the assistants

    self.delete_all_assistants()

  def get_all_assistants(self):
    return self.client.beta.assistants.list().data

  def get_all_files(self):
    return self.client.files.list().data


  # getters
  def get_file_path(self):
    return self.file_path

  def get_model(self):
    return self.model

  def get_system_intructions(self):
    return self.system_instructions

  def get_thread_instructions(self):
    return self.thread_instructions

  def get_tools(self):
    return self.tools

  def get_file_purpose(self):
    return self.file_purpose

  def get_assistnt_name(self):
    return self.assistant_name

  def get_key(self):
    return self.api_key

  def get_file_obj(self):
    return self.file

  def get_assistant_obj(self):
    return self.assistant

  def get_thread_obj(self):
    return self.thread


