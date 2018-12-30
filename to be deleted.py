# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 10:31:18 2018

@author: USER
"""

import facebook

token = 'EAAP9BZCFFLkMBAIAmR86qyNdDRUVT8k0zB5842b64LDIY3wzwCONcrJQywqv2fHp4DHUxGNEhqSr5DDtJ4hPTE7urIgzqVykkbVW3b9Tgdg7p00yqPRdJIz4ioAjcyRgKbkzvy6wPZAdymswkptlDrGwxVxoyG0nJhjn8CaimydNV7a3ym'
def main():
    graph = facebook.GraphAPI(access_token=token, version='2.8')
     # Write 'Hello, world' to the active user's wall.
    graph.put_object(parent_object='me', connection_name='feed',
                  message='Hello, world')

    # Add a link and write a message about it.
    graph.put_object(
       parent_object="me",
       connection_name="feed",
       message="This is a great website. Everyone should visit it.",
       link="https://www.facebook.com")

     # Write a comment on a post.
    graph.put_object(parent_object='post_id', connection_name='comments',
                  message='First!')