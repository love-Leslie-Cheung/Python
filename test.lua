#!/usr/bin/env lua 
function th_table_dup(ori_tab)                      -- 复制table
    if (type(ori_tab) ~= "table") then
        return nil;
    end
    local new_tab = {};
    for i,v in pairs(ori_tab) do
        local vtyp = type(v);
        if (vtyp == "table") then
            new_tab[i] = th_table_dup(v);
        elseif (vtyp == "thread") then
            -- TODO: dup or just point to?
            new_tab[i] = v;
        elseif (vtyp == "userdata") then
            -- TODO: dup or just point to?
            new_tab[i] = v;
        else
            new_tab[i] = v;
        end
    end
    return new_tab;
end
 
function permutation(s1,p)
    if #s1 == 1 then                                -- 如果s1长度为1，意味着获得了一种新的排列
        p = p .. (p~='' and ',' or '') .. s1[1]                              -- 那么就打印它
        print('{' .. p .. '}')
    else                                            -- 否则，选定一种方案，继续递归
        local i
        for i = 1, #s1 do                           -- 4.3 Control Structure; Numeric for
            local p2, s2
            p2 = p .. (p~='' and ',' or '') .. s1[i]
            s2 = th_table_dup(s1)                   -- 把s1表的内容复制给s2表
            table.remove(s2,i)                      -- 20.1 Insert and Remove
            permutation(s2,p2)                      -- 用s2继续进行递归
        end
    end
end
 
-- 主程序
-- a = io.read()                                       -- 读入字符串，可含汉字
--                                                     -- 22.1 The Simple I/O Model
-- len = #(string.gsub(a, "[\128-\191]", ""))          -- 计算字符数（不是字节数）
 
-- i=1                                                 -- 迭代出每一个字符，并保存在table中
-- s = {}                                              -- 21.1 Basic String Functions
-- for c in string.gmatch(a, ".[\128-\191]*") do       -- 21.2 Pattern-Matching Functions
--     s[i]=c                                          -- 21.7 Unicode
--     i=i+1
-- end
s = {1,2,3}
print("permutation output:")
p= ''
permutation(s,p)    