--------------------------------------------------
-- POP count gate
-- kadupitiya@kadupitiya.lk
--------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity num_ones_for is
    Port ( A : in  STD_LOGIC_VECTOR (15 downto 0);
           ones : out  STD_LOGIC_VECTOR (4 downto 0));
end num_ones_for;

architecture Behavioral of num_ones_for is

begin

process(A)
variable count : unsigned(4 downto 0) := "00000";
begin
    count := "00000";  
    for i in 0 to 15 loop  
        if(A(i) = '1') then 
            count := count + 1; 
        end if;
    end loop;
    ones <= std_logic_vector(count);
end process;

end Behavioral;