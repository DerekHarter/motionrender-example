all : harter-lu-motionrender-2023.pdf

harter-lu-motionrender-2023.pdf : harter-lu-motionrender-2023.tex
	pdflatex harter-lu-motionrender-2023.tex
	bibtex harter-lu-motionrender-2023
	pdflatex harter-lu-motionrender-2023.tex
	pdflatex harter-lu-motionrender-2023.tex

.PHONY : clean
clean  :
	rm -rf harter-lu-motionrender-2023.pdf *.aux *.bbl *.blg *.log *.out
