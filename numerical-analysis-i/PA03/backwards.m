% Author: Viet Duc Nguyen
% Date: 02.12.2018
% Solves the equation: piv(Rx) = piv(z)
function x = backwards(R,piv,z)
  n = length(R);
  x = zeros(n,1);
  Pz = z(piv);
  
  for k=n:-1:1
    x(k) = Pz(k);
    for j=k+1:n
      x(k) = x(k) - R(k,j)*x(j);
    end
    x(k) = x(k) / R(k,k);
  end
end
