--------------------------------------------------
-- XNOR gate Tester	
-- kadupitiya@kadupitiya.lk	
--------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

--------------------------------------------------

entity XNOR_ent_TEST is
end XNOR_ent_TEST;  

--------------------------------------------------

ARCHITECTURE behavior OF XNOR_ent_TEST IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT XNOR_ent
    port(	
		x: in std_logic;
		y: in std_logic;
		F: out std_logic
	);
    END COMPONENT;
    

   --Inputs
   signal x : std_logic := '0';
   signal y : std_logic := '0';

 	--Outputs
   signal F : std_logic;
 
   constant CLK_period : time := 20 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: XNOR_ent PORT MAP (
          x => x,
          y => y,
          F => F
        );

   -- Clock process definitions
   CLK_proc :process
   begin
		x <= '0';
		y <= '0';
		wait for CLK_period/4;
		x <= '0';
		y <= '1';
		wait for CLK_period/4;
		x <= '1';
		y <= '0';
		wait for CLK_period/4;
		x <= '1';
		y <= '1';
		wait for CLK_period/4;
   end process;
   
END;


--------------------------------------------------
