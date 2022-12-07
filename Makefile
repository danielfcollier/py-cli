install:
	@sudo ln -s ${PWD}/drageisa /usr/local/bin/drageisa

clean:
	@sudo rm /usr/local/bin/drageisa

update:
	@git pull
