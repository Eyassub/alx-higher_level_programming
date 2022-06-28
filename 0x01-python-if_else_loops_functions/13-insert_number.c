#include "lists.h"
#include <stdlib.h>
#include <unistd.h>
/**
* insert_node - inserts a number in an ordered linked list
* @head: double pointer to the linked list
* @number: number to insert in the new node
* Return: address of the new node, or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = NULL, *node = NULL;
if (head == NULL)
return (NULL);
node = malloc(sizeof(listint_t *));
if (node == NULL)
return (NULL);
node->next = NULL;
node->n = number;
temp = *head;
while (temp)
{
if (temp->n >= number)
{
node->next = temp;
*head = node;
return (node);
}
else if (temp->n <= number && temp->next->n >= number)
{
if (temp->next != NULL)
{
node->next = temp->next;
temp->next = node;
return (node);
}
}
temp = temp->next;
}
return (NULL);
}
