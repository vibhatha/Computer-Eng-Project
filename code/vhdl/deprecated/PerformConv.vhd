LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE STD.textio.ALL; --Dont forget to include this library for file operations.
USE ieee.std_logic_textio.ALL;

ENTITY read_matrix IS
END read_matrix;

ARCHITECTURE beha1 OF read_matrix IS

	COMPONENT XNORPOP IS
		PORT (
			A, B : IN std_logic_vector(8 DOWNTO 0);
			R : OUT std_logic_vector(8 DOWNTO 0);
			result : OUT INTEGER;
			Output : OUT std_logic
		);
	END COMPONENT; 
	CONSTANT c_WIDTH : NATURAL := 9;
	SIGNAL filter_bin : std_logic_vector(c_WIDTH - 1 DOWNTO 0) := "000000000";
	SIGNAL input_bin : std_logic_vector(c_WIDTH - 1 DOWNTO 0) := "010101011";
	--Inputs
	SIGNAL A : std_logic_vector(c_WIDTH - 1 DOWNTO 0) := "000000000";
	SIGNAL B : std_logic_vector(c_WIDTH - 1 DOWNTO 0) := "000000000";
 
	--Outputs
	SIGNAL R : std_logic_vector(c_WIDTH - 1 DOWNTO 0);
	SIGNAL Output : std_logic;
	SIGNAL result : INTEGER;
 
BEGIN
	--Call XNORPOP
	uut : XNORPOP
	PORT MAP(filter_bin, input_bin, R, result, Output); 

	--Read filter process
	PROCESS
	FILE file_pointer : text;
	VARIABLE line_content : STRING(1 TO c_WIDTH);
	VARIABLE line_num : line;
	VARIABLE j : INTEGER := 0;
	VARIABLE char : CHARACTER := '0';
	BEGIN
		--Open the file read_matrix.txt from the specified location for reading(READ_MODE).
		file_open(file_pointer, "/home/ise/Desktop/Project/filter.txt", READ_MODE); 
		WHILE NOT endfile(file_pointer) LOOP --till the end of file is reached continue.
		readline (file_pointer, line_num); --Read the whole line from the file
		--Read the contents of the line from the file into a variable.
		READ (line_num, line_content);
		--For each character in the line convert it to binary value.
		--And then store it in a signal named 'filter_bin'.
		FOR j IN 1 TO c_WIDTH LOOP 
			char := line_content(j);
			IF (char = '0') THEN
				filter_bin(c_WIDTH - j) <= '0';
			ELSE
				filter_bin(c_WIDTH - j) <= '1';
			END IF;
		END LOOP; 
		WAIT FOR 10 ns; --after reading each line wait for 10ns.
	END LOOP;
	file_close(file_pointer); --after reading all the lines close the file. 
	WAIT;
	END PROCESS;

	--Read input process
	PROCESS
	FILE file_pointer : text;
	FILE file_pointer_output : text;
	VARIABLE line_content : STRING(1 TO c_WIDTH);
	VARIABLE line_num : line;
	VARIABLE line_num_output : line;
	VARIABLE j : INTEGER := 0;
	VARIABLE char : CHARACTER := '0';
	BEGIN
		--Open the file read_matrix.txt from the specified location for reading(READ_MODE).
		file_open(file_pointer, "/home/ise/Desktop/Project/input.txt", READ_MODE);
		file_open(file_pointer_output, "/home/ise/Desktop/Project/output.txt", WRITE_MODE);
		WHILE NOT endfile(file_pointer) LOOP --till the end of file is reached continue.
		readline (file_pointer, line_num); --Read the whole line from the file
		--Read the contents of the line from the file into a variable.
		READ (line_num, line_content);
		--For each character in the line convert it to binary value.
		--And then store it in a signal named 'input_bin'.
		FOR j IN 1 TO c_WIDTH LOOP 
			char := line_content(j);
			IF (char = '0') THEN
				input_bin(c_WIDTH - j) <= '0';
			ELSE
				input_bin(c_WIDTH - j) <= '1';
			END IF;
		END LOOP; 
		WAIT FOR 10 ns; --after reading each line wait for 10ns.

		A <= filter_bin;
		B <= input_bin; 
 
		WAIT FOR 10 ns; --wait for 10ns get XNORPOP result. 
 
		write(line_num_output, Output, right, 1);
		writeline(file_pointer_output, line_num_output);
	END LOOP;
	file_close(file_pointer); --after reading all the lines close the file.
	file_close(file_pointer_output); --after reading all the lines close the file. 
	WAIT;
	END PROCESS;
END beha1;