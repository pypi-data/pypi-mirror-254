; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [5 x i8] c"Tag0\00"

define void @signed_cmp_test() local_unnamed_addr #0 {
entry:
  %0 = icmp sge i64 2, 1
  call void @__quantum__rt__bool_record_output(i1 %0, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @0, i32 0, i32 0))
  ret void
}

declare void @__quantum__rt__bool_record_output(i1, i8*)

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
