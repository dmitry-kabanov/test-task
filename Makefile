.PHONY : all
all :
	pip install -e .

.PHONY : build_ext
	python setup.py build_ext --inplace

.PHONY : clean
clean :
	-rm -rf \
		src/optimize/functionals.c \
		src/optimize/functionals.cpp \
		src/optimize/functionals.html \
		src/optimize/functionals.*.so \
		build
