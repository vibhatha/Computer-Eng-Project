--------------------------------------------------
-- XNORPOP gate
-- kadupitiya@kadupitiya.lk
--------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
--------------------------------------------------

ENTITY XNORPOP IS
	generic (N: positive := 64); --array size
	PORT (
		filter_bin, input_bin : IN std_logic_vector(N-1 DOWNTO 0);
		xnor_Result : OUT std_logic_vector(N-1 DOWNTO 0);
		pop_count : OUT INTEGER;
		scaled_result : OUT INTEGER;
		Output : OUT std_logic
	);
END XNORPOP;

--------------------------------------------------

ARCHITECTURE behav1 OF XNORPOP IS

	SIGNAL RTemp : std_logic_vector(N-1 DOWNTO 0);

BEGIN
	PROCESS
	VARIABLE temp : NATURAL := 0;
	VARIABLE pop_result : INTEGER := 0;
	BEGIN
		WAIT FOR 0.1 ns;
		temp := 0;
		RTemp <= filter_bin XNOR input_bin;
		xnor_Result <= RTemp;

		FOR i IN RTemp'RANGE LOOP
			IF RTemp(i) = '1' THEN
				temp := temp + 1;
			END IF;
		END LOOP;
		
		pop_count <= temp;
		
		pop_result := (2 * temp) - N;
		temp := 0;
		scaled_result <= pop_result;
 
		IF (pop_result > 0) THEN
			Output <= '1';
		ELSE
			Output <= '0';
		END IF;
	END PROCESS;

	END behav1;
	------------------------------------------------