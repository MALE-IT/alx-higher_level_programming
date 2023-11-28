#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: A pointer the head of the linked list.
 *@number: The number to insert.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	 listint_t *node = *head, *new_node;

	 new_node = malloc(sizeof(listint_t));

	 if (new_node == NULL)
	 {
		 return NULL;
	 }
}
