--------------------------------------------------
-- POP_Count Tester	
-- kadupitiya@kadupitiya.lk	
--------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use work.util.all;

--------------------------------------------------

entity POP_Counter_Test is
end POP_Counter_Test;  

--------------------------------------------------

ARCHITECTURE behavior OF POP_Counter_Test IS 
 
   --Inputs
   signal input : std_logic_vector(7 downto 0) := "00000000";
   --Outputs
   signal output : natural;
   constant CLK_period : time := 20 ns;
 
BEGIN

   -- Clock process definitions
   CLK_proc :process
   begin
		input <= "00000001";
		wait for 0.1 ns;
		output <= POP_Count (input);
		wait for CLK_period/2;
		input <= "00100101";
		wait for 0.1 ns;
		output <= POP_Count (input);
		wait for CLK_period/2;
		input <= "10100101";
		wait for 0.1 ns;
		output <= POP_Count (input);
		wait for CLK_period/2;
		input <= "11100101";
		wait for 0.1 ns;
		output <= POP_Count (input);
		wait for CLK_period/2;
		wait for 0.1 ns;
		input <= "11101101";
		wait for 0.1 ns;
		output <= POP_Count (input);
		wait for CLK_period/2;
   end process;
   
END;


--------------------------------------------------
