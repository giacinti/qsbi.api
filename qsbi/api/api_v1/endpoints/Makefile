.PHONY: all

codegen:= _codegen/codegen.py
template:= _codegen/templates/api_endpoint.j2

modules:= account 	\
	account_type 	\
	audit_log	\
	bank		\
	category	\
	currency	\
	currency_link	\
	party		\
	payment		\
	payment_type	\
	reconcile	\
	scheduled	\
	sub_category	\
	transact	\
	user


%.py: $(template)
	@python $(codegen) $(template) $(subst .py,,$@)

all: $(patsubst %,%.py,$(modules))

