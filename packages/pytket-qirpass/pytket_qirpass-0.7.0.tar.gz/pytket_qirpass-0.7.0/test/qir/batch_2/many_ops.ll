; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @classicalflow() local_unnamed_addr #0 {
entry:
  %0 = add i64 1, 2 ; 3
  call void @__quantum__rt__int_record_output(i64 %0)
  %1 = sub i64 6, 1 ; 5
  call void @__quantum__rt__int_record_output(i64 %1)
  %2 = udiv i64 4, 2 ; 2
  call void @__quantum__rt__int_record_output(i64 %2)
  %3 = mul i64 4, 2 ; 8
  call void @__quantum__rt__int_record_output(i64 %3)
  %4 = shl i64 1, 2 ; 4
  call void @__quantum__rt__int_record_output(i64 %4)
  %5 = lshr i64 4, 2 ; 1
  call void @__quantum__rt__int_record_output(i64 %5)
  %6 = xor i64 4, 2 ; 6
  call void @__quantum__rt__int_record_output(i64 %6)
  %7 = and i64 4, 2 ; 0
  call void @__quantum__rt__int_record_output(i64 %7)
  %8 = or i64 8, 2 ; 10
  call void @__quantum__rt__int_record_output(i64 %8)
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
