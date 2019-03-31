function y = qMult(QR,d,b)
  % n ... rows
  % m ... columns 
  [n,m] = size(QR);
  y = b;
  % calculate y = Q^T b
  for l=m:-1:1 % cols
    % Q = H_1^T H_2^T ... => Q^T = H_m ... H_2 H_1
    % H^T b = Eb - 2u^Tub = b - 2<u,u>b = b - 2*s*b            # (s = <u,u>)
    % Q^t b = H_m ... H_2 H_1 b = H_m ... H_2 (b - 2*s*u)
    
    % Calculate H^T(l)*y by formula H ^Tb
    % Construct vector u
    
    % householder matrices are symmetric
    u = [d(l); QR(l+1:n,l)];
    % calculate s = <u, u>
    s = 0;
    for k=l:n 
      s = s + u(k-l+1) * y(k); 
    end
    for k=l:n
      y(k) = y(k) - 2*s*u(k-l+1);
    end
  end 
end
