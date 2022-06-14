#include "lists.h"

/**
 * insert_node - insert node to a sorted linked list
 *
 * @head: the start of the linked list
 * @number: the integer in list
 * Return: address of node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *current, *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	prev = NULL, current = *head;
	if (current->n > number)	/* adds node to the beginning */
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current != NULL)
	{
		if (current->n > number)	/* adds node at an index */
		{
			prev->next = new;
			new->next = current;
			return (new);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new;	/* adds node to the end */
	return (new);
}
