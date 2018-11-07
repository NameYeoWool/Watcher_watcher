from seat_detect import Main2, image_generation

f0 = open('diff_check.txt','w')

for i in range(5):
    f0.write("Test Case no %d\n"%i)
    image_generation.imageGen()
    Main2.main()

    # Open file for reading in text mode (default mode)
    f1 = open('test.txt','r')
    f2 = open('output.txt','r')

    # Read the first line from the files
    f1_line = f1.readline()
    f2_line = f2.readline()

    # Initialize counter for line number
    line_no = 1

    # Loop if either file1 or file2 has not reached EOF
    while f1_line != '' or f2_line != '':

        # Strip the leading whitespaces
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()

        # Compare the lines from both file
        if f1_line != f2_line:

            # If a line does not exist on file2 then mark the output with + sign
            if f2_line == '' and f1_line != '':
                f0.write(">+")
                f0.write("Line-%d\n" % line_no)
                f0.write(f1_line)
            # otherwise output the line on file1 and mark it with > sign
            elif f1_line != '':
                f0.write(">")
                f0.write("Line-%d\n" % line_no)
                f0.write(f1_line)

            # If a line does not exist on file1 then mark the output with + sign
            if f1_line == '' and f2_line != '':
                f0.write("<+")
                f0.write("Line-%d\n" % line_no)
                f0.write(f2_line)
            # otherwise output the line on file2 and mark it with < sign
            elif f2_line != '':
                f0.write("<")
                f0.write("Line-%d\n" % line_no)
                f0.write(f2_line)

            # Print a blank line
            f0.write("\n")

        # Read the next line from the file
        f1_line = f1.readline()
        f2_line = f2.readline()

        # Increment line counter
        line_no += 1

    # Close the files
    f1.close()
    f2.close()