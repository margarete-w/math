mepsResult = meps();
maxResult = maximum();
minResult = minimum();


% MEPS  Find smallest number e such that 1+e > 1
%   We know that e = c*b^(1-p) with c in {0.5, 1} and let p be the exponent
%   mantissa length. Therefore, we get e by reducing the exponent
%   one by one. This is done by dividing by two.
function result = meps()
result = 1;
while (result+1 > 1)
   result = result/2;
end
result = result * 2;
end

% MAXIMUM   Find the biggest number that can be display by Matlab.
%   First, we increase the exponent to the biggest value possible by
%   iterating the series 2^n for n (starting with n=0). Then, we shift the
%   number from left until the number cannot be displayed anymore and inf
%   is returned, i.e. our number exceeds the number of significant bits
%   that can be saved.
function result = maximum()
result = 1;
expLength = 0;
% Find the biggest exponent
while (~isinf(2*result))
   expLength = expLength+1;
   result = 2*result;
end
% result should look like this 100..0 (the number has a bit length of expLengh+1)
% now we need to add some more one to the number so the bit pattern looks
% like this: 11111..1000...0
% The question is: How many one do we need to add after the most
% significant bit?

% For example: let 1000000000 be our biggest number so far (calculated as
% stated above). Now, shift the number to the right so we get 1100000000.
% If this new number is not infinity, we get a new maximum! Then, we
% consider 1110000000 and so on...
bitsToAdd = 2.^(expLength - 1);
while(~isinf(bitsToAdd + result))
    result = bitsToAdd + result;
    bitsToAdd = bitsToAdd / 2;
end
end


function result = minimum()
result = 1;
while (result / 2 ~= 0)
   result = result / 2;
end
end
