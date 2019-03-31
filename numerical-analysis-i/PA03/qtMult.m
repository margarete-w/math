% Author: Viet Duc Nguyen
% Date: 02.12.2018
%
% Apply the householder matrix Q^T on b.
% Input: QR ... 
%         d ...
%
% Output: y ... y = Q^Tb
function y = qtMult(QR,d,b)
  % n ... rows
  % m ... columns 
  [n,m] = size(QR);
  y = b;
  % calculate y = Q^T b
  for l=1:m % cols
    % Q = H_1^T H_2^T ... => Q^T = H_m ... H_2 H_1
    % H b = Eb - 2uu^Tb = b - 2u<u,b> = b - 2*s*u            # (s = <u,b>)
    % Q^t b = H_m ... H_2 H_1 b = H_n ... H_2 (b - 2*s*u)
    
    % Calculate H(l)*y by formula H b
    % Construct vector u
    u = [d(l); QR(l+1:n,l)];
    % calculate s = <y, u>
    s = 0;
    for k=l:n 
      s = s + y(k) * u(k-l+1); 
    end
    for k=l:n
      y(k) = y(k) - 2*s*u(k-l+1);
    end
  end 
end
% this algorithms runs in O(2*n*m) = O(n*m)