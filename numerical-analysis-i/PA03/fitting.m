% Author: Viet Duc Nguyen
% Date: 02.12.2018
% Solves the fitting problem
function [x,s] = fitting(M,y)
  [n,m] = size(M);
  [QR,d] = qrDecomposition(M);
  QTy = qtMult(QR,d,y);
  trimmedQR = QR(1:m, 1:m);
  x = backwards(trimmedQR, [1:m], QTy);
  
  % calculate the residual
  %{
  tdef(1:m) = zeros(1:m,1);
  tdef(m+1:n) = QTy(m+1:n);
  defect = qMult(QR, d, tdef);
  s = vecnorm(defect);
  %}
end
