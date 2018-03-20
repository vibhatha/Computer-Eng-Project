--------------------------------------------------
-- XNOR gate	
-- kadupitiya@kadupitiya.lk	
--------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

--------------------------------------------------

entity XNOR_ent is
port(	x: in std_logic;
	y: in std_logic;
	F: out std_logic
);
end XNOR_ent;  

--------------------------------------------------

architecture behav1 of XNOR_ent is
begin

    process(x, y)
    begin
        -- compare to truth table
    if ((x='0') and (y='0')) then
	    F <= '1';
	elsif ((x='1') and (y='1')) then
	    F <= '1';
	else
	    F <= '0';
	end if;
    end process;

end behav1;


--------------------------------------------------
