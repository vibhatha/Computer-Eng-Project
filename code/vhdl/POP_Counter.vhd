--------------------------------------------------
-- POP_Count Function	
-- kadupitiya@kadupitiya.lk	
--------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

package util is

	function POP_Count(input : std_logic_vector) return integer;

end;

package body util is

	function POP_Count(input : std_logic_vector) return integer is
	  variable temp : natural := 0;
	
	begin
	  for i in input'range loop
		if input(i) = '1' then temp := temp + 1; 
		end if;
	  end loop;
	  
	  return temp;
	  
	end function POP_Count;
	
end package body;

