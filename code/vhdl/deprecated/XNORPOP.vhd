--------------------------------------------------
-- XNORPOP gate
-- kadupitiya@kadupitiya.lk
--------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
--------------------------------------------------

ENTITY XNORPOP IS
	PORT (
		A, B : IN std_logic_vector(8 DOWNTO 0);
		R : OUT std_logic_vector(8 DOWNTO 0);
		result : OUT INTEGER;
		Output : OUT std_logic
	);
END XNORPOP;

--------------------------------------------------

ARCHITECTURE behav1 OF XNORPOP IS

	SIGNAL RTemp : std_logic_vector(8 DOWNTO 0) := "000000000";

BEGIN
	PROCESS
	VARIABLE temp : NATURAL := 0;
	VARIABLE pop_result : INTEGER := 0;
	BEGIN
		WAIT FOR 0.1 ns;
		temp := 0;
		RTemp <= A XNOR B;
		R <= RTemp;

		FOR i IN RTemp'RANGE LOOP
			IF RTemp(i) = '1' THEN
				temp := temp + 1;
			END IF;
		END LOOP;
 
		pop_result := (2 * temp) - 9;
		temp := 0;
		result <= pop_result;
 
		-- compare to truth table
		IF (pop_result > 0) THEN
			Output <= '1';
		ELSE
			Output <= '0';
		END IF;
	END PROCESS;

	END behav1;
	------------------------------------------------