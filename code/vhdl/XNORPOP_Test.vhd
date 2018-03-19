--------------------------------------------------
-- POP_Count Tester	
-- kadupitiya@kadupitiya.lk	
--------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

--------------------------------------------------

entity XNORPOP_Test is
end XNORPOP_Test;  

--------------------------------------------------

ARCHITECTURE behavior OF XNORPOP_Test IS 


	COMPONENT XNORPOP is
	PORT (
		A, B : IN std_logic_vector(8 DOWNTO 0);
		R : OUT std_logic_vector(8 DOWNTO 0);
		result : OUT integer;
		Output : OUT std_logic
	);
	end COMPONENT;  
 
   --Inputs
   signal A : std_logic_vector(8 downto 0) := "000000000";
   signal B : std_logic_vector(8 downto 0) := "000000000";

 	--Outputs
   signal R : std_logic_vector(8 downto 0);
   signal Output : std_logic;
   signal result : integer;
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 
   constant x_period : time := 100 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: XNORPOP PORT MAP (A, B, R, result, Output);

   -- Clock process definitions
   add_process :process
   begin
		A <= "000000000";
		B <= "000000000";
		wait for x_period/2;
		A <= "110110111";
		B <= "010111010";
		wait for x_period/2;
		A <= "111111111";
		B <= "000000000";
		wait for x_period/2;
		A <= "111111111";
		B <= "000000001";
		wait for x_period/2;
		A <= "111111111";
		B <= "000000011";
		wait for x_period/2;
		A <= "111111111";
		B <= "000000111";
		wait for x_period/2;
		A <= "111111111";
		B <= "000001111";
		wait for x_period/2;
		A <= "111111111";
		B <= "000011111";
		wait for x_period/2;
		A <= "111111111";
		B <= "000111111";
		wait for x_period/2;
		A <= "111111111";
		B <= "001111111";
		wait for x_period/2;
		A <= "111111111";
		B <= "011111111";
		wait for x_period/2;
		A <= "111111111";
		B <= "111111111";
		wait for x_period/2;

   end process;

END;


--------------------------------------------------
