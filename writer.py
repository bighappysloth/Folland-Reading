chapter_number = input("Chapter number: ")
theorem_max = input("Theorem Max: ")

for i in range(1,int(theorem_max)+1):
	output_name = 'Theorem' + str(chapter_number) + '_' + str(i) + ".tex"
	print(output_name)

	# Write a file
	with open(output_name, "w") as file:
		subsection_string = 'Theorem ' + str(chapter_number) + '.' + str(i)

		file_contents = r'''\documentclass[../../main.tex]{subfiles}

\begin{document}
\subsection{''' + subsection_string + r'''}
\begin{wts}

\end{wts}
\begin{proof}

\end{proof}

\end{document}'''
		print(file_contents)
		file.write(file_contents)