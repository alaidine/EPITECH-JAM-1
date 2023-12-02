##
## EPITECH PROJECT, 2023
## Makefile
## File description:
## Makefile
##

SRC	=	checkers.py

NAME	=	checkers

all:
	cp $(SRC) $(NAME)
	chmod 777 $(NAME)

clean:
	rm -f $(NAME)

fclean:	clean
	rm -f *~

re:	fclean all
