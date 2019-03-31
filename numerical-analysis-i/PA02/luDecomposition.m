% Program for LU decomposition
% Author: Viet Duc Nguyen
% Date: 01.12.2018
% Input: matrix A
% Output: [LU,z]... where a is the matrix whose values above the diagonal is an upper right matrix
%                   and below the diagonal it is an lower left matrix
%                   z contains the executed permutations
function [LU,z] = luDecomposition(A)
LU = A;
n = length(LU);
if (det(LU) == 0)
    disp('Matrix not invertible');
end
% initialisation of the vector saving the permutations
% note that z is a row vector
z = 1:n;
% Elimination
for j=1:n-1
    % find the pivot
    % the pivot is the row with largest head element
   pivot = LU(j,j);
   pivIdx = j;
   for l=j+1:n
      if (abs(LU(l,j)) > abs(pivot))
          pivot = LU(l,j);
          pivIdx = l;
      end
   end
   % swap rows j and pivIdx
   LU([j, pivIdx],:) = LU([pivIdx, j], :);
   % update permutation vector
   z([j,pivIdx]) = z([pivIdx,j]);
   % Elimination
   for i = j+1:n
      LU(i,j) = LU(i,j) / LU(j,j);
      for k = j+1:n
          LU(i,k) = LU(i,k) - LU(i,j) * LU(j,k);
      end
   end
end
% transpose the permutation vector
% z = z';
end
