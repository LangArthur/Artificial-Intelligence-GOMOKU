NAME	=	pbrain-gomoku-ai

all:
	cp pbrain-gomoku-ai.py $(NAME)
	chmod 777 $(NAME)

build-exe:
	cd output/$(NAME) && pyinstaller -y  "C:/Users/Arthur LANG/delivery/Artificial_intelligence/AIA_gomoku_2019/pbrain-gomoku-ai.py"

clean:
	rm -f $(NAME)

fclean: clean

re: fclean all

.PHONY:
	all, clean, fclean, re
