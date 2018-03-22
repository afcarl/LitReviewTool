import os

def lists_to_delete():
  pkl_to_delete = [f for f in os.listdir() if f.endswith('.pkl')]
  uid_to_delete = [i for i in os.listdir() if 'unique_identifier_' in i and i.endswith('.json')]
  to_delete = uid_to_delete+pkl_to_delete
  return to_delete


def main():
  to_delete = lists_to_delete()
  
  for f in to_delete:
    os.remove(f)

  
if __name__ == '__main__':
  main()
