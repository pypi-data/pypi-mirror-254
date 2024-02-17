; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @classicalflow() local_unnamed_addr #0 {
entry:
  %0 = or i1 1, 0 ; 1
  call void @__quantum__rt__bool_record_output(i1 %0)
  %1 = xor i1 1, 1 ; 0
  call void @__quantum__rt__bool_record_output(i1 %1)
  %2 = icmp eq i1 %0, %1 ; 0
  call void @__quantum__rt__bool_record_output(i1 %2)
  %3 = icmp ne i1 %0, %1 ; 1
  call void @__quantum__rt__bool_record_output(i1 %3)
  %4 = icmp ult i1 %0, %1 ; 0
  call void @__quantum__rt__bool_record_output(i1 %4)
  %5 = icmp ule i1 %0, %1 ; 0
  call void @__quantum__rt__bool_record_output(i1 %5)
  %6 = icmp ugt i1 %0, %1 ; 1
  call void @__quantum__rt__bool_record_output(i1 %6)
  %7 = icmp uge i1 %0, %1 ; 1
  call void @__quantum__rt__bool_record_output(i1 %7)
  ret void
}

declare void @__quantum__rt__bool_record_output(i1) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
