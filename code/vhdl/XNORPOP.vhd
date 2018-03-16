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
		result : OUT integer;
		Output : OUT std_logic
	);
END XNORPOP; 

--------------------------------------------------

ARCHITECTURE behav1 OF XNORPOP IS

	signal RTemp : std_logic_vector(8 downto 0) := "000000000";

BEGIN
	PROCESS
	variable temp : natural := 0;
	VARIABLE pop_result : integer := 0;
	BEGIN
		wait for 0.1 ns;
		temp := 0;
		RTemp <= A XNOR B;
		R <= RTemp;

		for i in RTemp'range loop
			if RTemp(i) = '1' then temp := temp + 1; 
			end if;
		end loop;
		
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